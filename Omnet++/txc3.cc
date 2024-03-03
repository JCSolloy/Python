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

using namespace omnetpp; // This is the namespace which contains all OMNeT++-related stuff.

/**
 * In this class we add a counter, and delete the message after ten exchanges.
 */
class Txc3 : public cSimpleModule // cSimpleModule is the base class for all simple modules.
{
  private:// The following members are private and thus not visible to the derived modules.
    int counter;  // Note the counter here

  protected:// The following members are protected and thus visible to the derived modules.
    virtual void initialize() override;// This method is called once at the beginning of the simulation.
    virtual void handleMessage(cMessage *msg) override;// This method is called whenever a message arrives at the module.
};

Define_Module(Txc3);// This is a macro that registers the class with the OMNeT++ type system.

void Txc3::initialize()
{
    // Initialize counter to ten. We'll decrement it every time and delete
    // the message when it reaches zero.
    counter = 10;// Initialize counter to ten.

    // The WATCH() statement below will let you examine the variable under
    // Qtenv. After doing a few steps in the simulation, click either
    // `tic' or `toc', and you'll find its `counter' variable and its
    // current value displayed in the inspector panel (bottom left).
    WATCH(counter);// WATCH is a macro that expands to getSimulation()->getEnvir()->addWatch().

    if (strcmp("tic", getName()) == 0) { // strcmp is a standard C function that compares two strings.
        EV << "Sending initial message\n"; // EV is a macro that expands to getSimulation()->getEnvir()->log().
        cMessage *msg = new cMessage("tictocMsg");//cMessage is a class that represents a message in the simulation.
        send(msg, "out"); // send out the message
    }
}

void Txc3::handleMessage(cMessage *msg)
{
    // Increment counter and check value.
    counter--; // Decrement counter.
    if (counter == 0) {// If counter is zero, delete message.
        // If counter is zero, delete message. If you run the model, you'll
        // find that the simulation will stop at this point with the message
        // "no more events".
        EV << getName() << "'s counter reached zero, deleting message\n"; // EV is a macro that expands to getSimulation()->getEnvir()->log().
        delete msg;// delete the message
    }
    else {
        EV << getName() << "'s counter is " << counter << ", sending back message\n"; // EV is a macro that expands to getSimulation()->getEnvir()->log().
        send(msg, "out");
    }
}

