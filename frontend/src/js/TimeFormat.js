function formatTimestamp(timestamp) {
    const date = new Date(timestamp)
    const now = new Date()

    // Otherwise, show date and time
    return `${date.toLocaleDateString()} ${date.toLocaleTimeString()}`;
}

export default formatTimestamp;
