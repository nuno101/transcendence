function formatTimestamp(timestamp) {
    const date = new Date(timestamp)
    const now = new Date()

    // If today, show "Today" and time
    if (date.toDateString() === now.toDateString()) {
        return `Today ${date.toLocaleTimeString()}`;
    }

    // If yesterday, show "Yesterday" and time
    const yesterday = new Date(now)
    yesterday.setDate(now.getDate() - 1)
    if (date.toDateString() === yesterday.toDateString()) {
        return `Yesterday ${date.toLocaleTimeString()}`;
    }

    // Otherwise, show date and time
    return `${date.toLocaleDateString()} ${date.toLocaleTimeString()}`;
}

export default formatTimestamp;