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
 * In this step you'll learn how to add input parameters to the simulation:
 * we'll turn the "magic number" 10 into a parameter.
 */
class Txc4 : public cSimpleModule // cSimpleModule is the base class for all simple modules.
{
  private: // The following members are private and thus not visible to the derived modules.
    int counter; // Note the counter here

  protected: // The following members are protected and thus visible to the derived modules.
    virtual void initialize() override;
    virtual void handleMessage(cMessage *msg) override;
};

Define_Module(Txc4); // This is a macro that registers the class with the OMNeT++ type system.

void Txc4::initialize()
{
    // Initialize the counter with the "limit" module parameter, declared
    // in the NED file (tictoc4.ned).
    counter = par("limit"); // par is a method that returns the value of a parameter.

    // we no longer depend on the name of the module to decide
    // whether to send an initial message
    if ( par("sendMsgOnInit").boolValue() == true) { 
        // par is a method that returns the value of a parameter.

        EV << "Sending initial message\n";
        cMessage *msg = new cMessage("tictocMsg");
        send(msg, "out");
    }
}

void Txc4::handleMessage(cMessage *msg)
{
    counter--;
    if (counter == 0) {
        EV << getName() << "'s counter reached zero, deleting message\n";
        delete msg;
    }
    else {
        EV << getName() << "'s counter is " << counter << ", sending back message\n";
        send(msg, "out");
    }
}
