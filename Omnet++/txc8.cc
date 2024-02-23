#include <stdio.h>
#include <string.h>
#include <omnetpp.h>

using namespace omnetpp;

/**
 * Let us take a step back, and remove random delaying from the code.
 * We'll leave in, however, losing the packet with a small probability.
 * And, we'll we do something very common in telecommunication networks:
 * if the packet doesn't arrive within a certain period, we'll assume it
 * was lost and create another one. The timeout will be handled using
 * (what else?) a self-message.
 */
class Tic8 : public cSimpleModule //Tic8 is the sender module
{
  private: // The following members are used to keep track of the packet and the timeout event.
    simtime_t timeout;  // timeout // time after which the packet is considered lost
    cMessage *timeoutEvent = nullptr;  // holds pointer to the timeout self-message 
    // if the packet is not received within the timeout, the packet is considered lost and a new packet is sent

  public:
    virtual ~Tic8();

  protected:
    virtual void initialize() override;
    virtual void handleMessage(cMessage *msg) override;
};

Define_Module(Tic8); //Tic8 is the sender module

Tic8::~Tic8() //destructor
{
    cancelAndDelete(timeoutEvent);
}

void Tic8::initialize()//initialize function is called when the simulation starts
{
    // Initialize variables.
    timeout = 1.0;// timeout is set to 1.0
    timeoutEvent = new cMessage("timeoutEvent"); //create a new message for timeout event

    // Generate and send initial message.
    EV << "Sending initial message\n"; 
    //EV is a macro that is used to print the message to the console
    cMessage *msg = new cMessage("tictocMsg"); //create a new message
    //tictocMsg is the name of the message
    send(msg, "out"); //send the message to the output gate
    scheduleAt(simTime()+timeout, timeoutEvent); // schedule the timeout event
    //simTime() returns the current simulation time
    // Tiempo actual + tieme out = tiempo en el que se va a ejecutar el evento
    //scheduleAt function is used to schedule the timeout event
}

void Tic8::handleMessage(cMessage *msg)
{
    if (msg == timeoutEvent) {
// If we receive the timeout event, that means the packet hasn't arrived in time and we have to re-send it.
        // If we receive the timeout event, that means the packet hasn't
        // arrived in time and we have to re-send it.
        EV << "Timeout expired, resending message and restarting timer\n";
        cMessage *newMsg = new cMessage("tictocMsg"); //create a new message for resending
        send(newMsg, "out");
        scheduleAt(simTime()+timeout, timeoutEvent);
        //scheduleAt function is used to schedule the timeout event
    }
    else {  // message arrived
            // Acknowledgement received -- delete the received message and cancel
            // the timeout event.
        EV << "Timer cancelled.\n";// Print the message to the console
        cancelEvent(timeoutEvent);// Cancel the timeout event 
        delete msg;// Delete the message

        // Ready to send another one.
        cMessage *newMsg = new cMessage("tictocMsg");// Create a new message 
        send(newMsg, "out");
        scheduleAt(simTime()+timeout, timeoutEvent);
    }
}

/**
 * Sends back an acknowledgement -- or not.
 */
class Toc8 : public cSimpleModule
{
  protected:
    virtual void handleMessage(cMessage *msg) override;
};

Define_Module(Toc8);

void Toc8::handleMessage(cMessage *msg)
{
    if (uniform(0, 1) < 0.1) {
        EV << "\"Losing\" message.\n";
        bubble("message lost");  // making animation more informative...
        delete msg;
    }
    else {
        EV << "Sending back same message as acknowledgement.\n";
        send(msg, "out");
    }
}
