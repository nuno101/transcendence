import Notifications from '../Notifications'

// TODO: Add structure to define a function/event handler for each event that is being
// by the websocket event handler

export async function wsEventHandler(event) {
    console.log(event)

    // TODO: Use Structure here to decide which function to forward the event to

    // TODO: Instead of checking here if the page reload message should be displayed move this
    // functionality into the event handlers for specific events and sites
    // Post Event if event happens not on current page
    if(!Notifications.checkPageAndEvents(window.location.pathname, JSON.parse(event.data).event))
        await Notifications.postNotification(event.data);
}
// ----------------------------------------------------------------------------------------------------

// INFO: Placeholder function where a potential game event handler could be implemented
export async function wsGameHandler(event) {}