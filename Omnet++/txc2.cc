//
// This file is part of an OMNeT++/OMNEST simulation example.
//
// Copyright (C) 2003 Ahmet Sekercioglu
// Copyright (C) 2003-2015 Andras Varga
//
// This file is distributed WITHOUT ANY WARRANTY. See the file
// `license' for details on this and other legal matters.
//

#include <string.h>
#include <omnetpp.h>

using namespace omnetpp;

/**
 * In this step we add some debug messages to Txc1. When you run the
 * simulation in the OMNeT++ Qtenv GUI, the log will appear in the bottom
 * panel of the Qtenv window. To see only the log from `tic' or `toc' alone,
 * go into them by double-clicking their icons, and the bottom panel will
 * be filtered accordingly. (You can go back with the up arrow button on
 * the toolbar.)
 */
class Txc2 : public cSimpleModule // cSimpleModule is the base class for all simple modules. 
// public means that the members of cSimpleModule are accessible from Txc2.

{
  protected: // The following members are protected and thus visible to the derived modules.
    virtual void initialize() override;
    virtual void handleMessage(cMessage *msg) override;
};

Define_Module(Txc2); // This is a macro that registers the class with the OMNeT++ type system.

void Txc2::initialize()// This method is called once at the beginning of the simulation.
{
    if (strcmp("tic", getName()) == 0) { // strcmp is a standard C function that compares two strings.
        // The `ev' object works like `cout' in C++.
        EV << "Sending initial message\n"; // EV is a macro that expands to getSimulation()->getEnvir()->log().
        cMessage *msg = new cMessage("tictocMsg"); //cMessage is a class that represents a message in the simulation.
        send(msg, "out");// send out the message
    }
}

void Txc2::handleMessage(cMessage *msg)
{
    // msg->getName() is name of the msg object, here it will be "tictocMsg".
    EV << "Received message `" << msg->getName() << "', sending it out again\n"; 
    // EV is a macro that expands to getSimulation()->getEnvir()->log().

    send(msg, "out");
}

