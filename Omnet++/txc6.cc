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
 * In the previous models, `tic' and `toc' immediately sent back the
 * received message. Here we'll add some timing: tic and toc will hold the
 * message for 1 simulated second before sending it back. In OMNeT++
 * such timing is achieved by the module sending a message to itself.
 * Such messages are called self-messages (but only because of the way they
 * are used, otherwise they are completely ordinary messages) or events.
 * Self-messages can be "sent" with the scheduleAt() function, and you can
 * specify when they should arrive back at the module.
 *
 * We leave out the counter, to keep the source code small.
 */
class Txc6 : public cSimpleModule // cSimpleModule is the base class for all simple modules
{
  private: // The following members are private and thus not visible to the derived modules.
    // Set the pointers to nullptr, so that the destructor won't crash
    // even if initialize() doesn't get called because of a runtime
    // error or user cancellation during the startup process.
    cMessage *event = nullptr;  // pointer to the event object which we'll use for timing
    cMessage *tictocMsg = nullptr;  // variable to remember the message until we send it back
// nullptr is a special pointer value that is used to indicate that the pointer is not pointing to any valid object.

  public:// The following members are public and thus visible to the derived modules.

    virtual ~Txc6(); // virtual destructor  
// The destructor is virtual so that the destructor of the derived class is called when the object is deleted.


  protected:// The following members are protected and thus visible to the derived modules.
    virtual void initialize() override; // The initialize() method is called at the beginning of the simulation.
    virtual void handleMessage(cMessage *msg) override; // The handleMessage() method is called whenever a message arrives at the module.
};

Define_Module(Txc6);// With this macro, the module class is registered in the OMNeT++ system.

Txc6::~Txc6()
// The destructor is called when the simulation is over. It is used to release the resources acquired by the module during the simulation.
{
    // Dispose of dynamically allocated the objects
    cancelAndDelete(event); // cancelAndDelete() cancels the event and deletes it from the event list.
    delete tictocMsg; // delete the message object
}

void Txc6::initialize()// The initialize() method is called at the beginning of the simulation.
{
    // Create the event object we'll use for timing -- just any ordinary message.
    event = new cMessage("event");// Create a new message object and assign it to the event pointer.

    // No tictoc message yet.
    tictocMsg = nullptr; // nullptr is a special pointer value that is used to indicate that the pointer is not pointing to any valid object.

    if (strcmp("tic", getName()) == 0) {
        // strcmp() compares two strings and returns 0 if they are equal. getName() returns the name of the module.
        // We don't start right away, but instead send an message to ourselves
        // (a "self-message") -- we'll do the first sending when it arrives
        // back to us, at t=5.0s simulated time.
        EV << "Scheduling first send to t=5.0s\n";// EV is a macro that is used to print out messages to the console.
        tictocMsg = new cMessage("tictocMsg");// Create a new message object and assign it to the tictocMsg pointer.
        scheduleAt(5.0, event);// scheduleAt() schedules the event to be sent to the module at the specified time.
    }
}

void Txc6::handleMessage(cMessage *msg)// The handleMessage() method is called whenever a message arrives at the module.
{
    // There are several ways of distinguishing messages, for example by message
    // kind (an int attribute of cMessage) or by class using dynamic_cast
    // (provided you subclass from cMessage). In this code we just check if we
    // recognize the pointer, which (if feasible) is the easiest and fastest
    // method.
    if (msg == event) {
        // If the message is the self-message, then we send out tictocMsg and nullptr out its pointer so that it doesn't confuse us later.
        // The self-message arrived, so we can send out tictocMsg and nullptr out
        // its pointer so that it doesn't confuse us later.
        EV << "Wait period is over, sending back message\n";// EV is a macro that is used to print out messages to the console.
        send(tictocMsg, "out");// send() sends the message to the specified gate.
        tictocMsg = nullptr;// nullptr is a special pointer value that is used to indicate that the pointer is not pointing to any valid object.
    }
    else {
        // If the message is not the self-message, then we remember its pointer in the tictocMsg variable, 
        // then schedule our self-message to come back to us in 1s simulated time.
        // If the message we received is not our self-message, then it must
        // be the tic-toc message arriving from our partner. We remember its
        // pointer in the tictocMsg variable, then schedule our self-message
        // to come back to us in 1s simulated time.
        EV << "Message arrived, starting to wait 1 sec...\n";// EV is a macro that is used to print out messages to the console.
        tictocMsg = msg;// Remember the message
        scheduleAt(simTime()+1.0, event);// scheduleAt() schedules the event to be sent to the module at the specified time.
    }
}