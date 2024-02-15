import Backend from './Backend';

class Avatar {
    static getAvatarById = async (id) => {
        try {
            const avatar = await Backend.getAvatar(`/api/users/${id}/avatar`);
            return avatar;
        } catch (err) {
            console.error(err.message);
            return null;
        }
    };
}

export default Avatar
