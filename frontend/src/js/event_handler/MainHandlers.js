import Notifications from '../Notifications'
import Chat from '../Chat'

// TODO: Add structure to define a function/event handler for each event that is being
// by the websocket event handler

const handlers = {
    "create_message": Chat.createMessage,
    "delete_message": Chat.deleteMessage,
}

export async function wsEventHandler(event) {
    event = JSON.parse(event.data);
    console.log(event)

    for (const [key, value] of Object.entries(handlers)) {
        if (event.event === key) {
            await value(event);
        }
    }

    // TODO: Instead of checking here if the page reload message should be displayed move this
    // functionality into the event handlers for specific events and sites
    // Post Event if event happens not on current page
    // if(!Notifications.checkPageAndEvents(window.location.pathname, JSON.parse(event.data).event))
    //     await Notifications.postNotification(event.data);
}
// ----------------------------------------------------------------------------------------------------

// INFO: Placeholder function where a potential game event handler could be implemented
export async function wsGameHandler(event) {}