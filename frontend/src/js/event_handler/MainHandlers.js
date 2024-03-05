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
}
// ----------------------------------------------------------------------------------------------------

// INFO: Placeholder function where a potential game event handler could be implemented
export async function wsGameHandler(event) {}