import Backend from './Backend';

class Helpers {
    static getAvatarById = async (id) => {
        try {
            const avatar = await Backend.getAvatar(`/api/users/${id}/avatar`);
            return avatar;
        } catch (err) {
            console.error(err.message);
            return null;
        }
    };

    static getAvatarUrl = (id) => {
        return Helpers.getAvatarById(id);
    };
}

export default Helpers
