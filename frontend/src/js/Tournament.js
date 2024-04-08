import Notifications from './Notifications';

class Tournament {
  static starting = async (data) => {
    await Notifications.post(data);
  }
}

export default Tournament