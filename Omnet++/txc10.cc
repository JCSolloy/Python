#include <stdio.h>
#include <string.h>
#include <omnetpp.h>

using namespace omnetpp;

/**
 * Let's make it more interesting by using several (n) `tic' modules,
 * and connecting every module to every other. For now, let's keep it
 * simple what they do: module 0 generates a message, and the others
 * keep tossing it around in random directions until it arrives at
 * module 2.
 */
class Txc10 : public cSimpleModule
{
  protected:
    virtual void forwardMessage(cMessage *msg);
    virtual void initialize() override;
    virtual void handleMessage(cMessage *msg) override;
};

Define_Module(Txc10);

void Txc10::initialize()
{
    if (getIndex() == 0) { // If I am the source of the message
        // Boot the process scheduling the initial message as a self-message.
        char msgname[20]; // Generate a message name.
        sprintf(msgname, "tic-%d", getIndex()); 
 // Generate a message name with the index of the module.
        cMessage *msg = new cMessage(msgname);
        scheduleAt(0.0, msg);
    }
}

void Txc10::handleMessage(cMessage *msg)
{
    if (getIndex() == 3) {
        // Message arrived.
        EV << "Message " << msg << " arrived.\n";
        delete msg;
    }
    else {
        // We need to forward the message.
        forwardMessage(msg);
    }
}

void Txc10::forwardMessage(cMessage *msg)
{
    // In this example, we just pick a random gate to send it on.
    // We draw a random number between 0 and the size of gate `out[]'.
    int n = gateSize("out");
    int k = intuniform(0, n-1);

    EV << "Forwarding message " << msg << " on port out[" << k << "]\n";
    send(msg, "out", k); 
    // send out on the k-th gate of the module (counting starts at 0) 
}