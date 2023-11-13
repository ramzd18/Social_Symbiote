// userdata.js
import { useState } from 'react';

const useUserData = () => {
  const [userdata, setUserdata] = useState({});

  return { userdata, setUserdata };
};

export default useUserData;
