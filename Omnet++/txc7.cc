//
// This file is part of an OMNeT++/OMNEST simulation example.
//
// Copyright (C) 2003-2015 Andras Varga
//
// This file is distributed WITHOUT ANY WARRANTY. See the file
// `license' for details on this and other legal matters.
//

#include <stdio.h>
#include <string.h>
#include <omnetpp.h>

using namespace omnetpp;

/**
 * In this step we'll introduce random numbers. We change the delay from 1s
 * to a random value which can be set from the NED file or from omnetpp.ini.
 * In addition, we'll "lose" (delete) the packet with a small probability.
 */
class Txc7 : public cSimpleModule
{
  private:
    cMessage *event = nullptr; // Pointer to the event object which we'll use for timing
    cMessage *tictocMsg = nullptr; // Pointer to the message object which we'll send

  public:
    virtual ~Txc7(); // Destructor is used to release the memory allocated for the message

  protected:
    virtual void initialize() override;// Initialize the module
    virtual void handleMessage(cMessage *msg) override;// Handle the message
};

Define_Module(Txc7);

Txc7::~Txc7() // Destructor
{
    cancelAndDelete(event);
    delete tictocMsg;
}

void Txc7::initialize() // Initialize the module and set the first event
{
    event = new cMessage("event"); // Create the event object
    tictocMsg = nullptr; // Initialize the message object

    if (strcmp("tic", getName()) == 0) { // If the module name is "tic"
        EV << "Scheduling first send to t=5.0s\n";// Print the message
        scheduleAt(5.0, event);// Schedule the first event at t=5.0s
        tictocMsg = new cMessage("tictocMsg");// Create the message object
    }
}

void Txc7::handleMessage(cMessage *msg) // Handle the message and send it back after a random delay
{
    if (msg == event) { // If the message is the event
        EV << "Wait period is over, sending back message\n"; // Print the message to the console
        send(tictocMsg, "out");// Send the message to the output gate
        tictocMsg = nullptr; // Set the message object to nullptr
    }
    else {
        // "Lose" the message with 0.1 probability:
        if (uniform(0, 1) < 0.1) { // If the random number is less than 0.1
            EV << "\"Losing\" message\n"; // Print the message to the console
            delete msg;
        }
        else {
            // The "delayTime" module parameter can be set to values like
            // "exponential(5)" (tictoc7.ned, omnetpp.ini), and then here
            // we'll get a different delay every time.
            simtime_t delay = par("delayTime");// Get the delay time from the module parameter "delayTime"
            //simtime_t delay = 1.0; // Constant delay

            EV << "Message arrived, starting to wait " << delay << " secs...\n";
            tictocMsg = msg;
            scheduleAt(simTime()+delay, event);
        }
    }
}