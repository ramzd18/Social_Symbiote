import ram_avatar from '../avatar_pictures/ram_avatar.png'
import Profile from './Profile.js'
import modules from './ProfileList.module.css'
import Card from 'react-bootstrap/Card';
function ProfileList() {
  const Profiles = [<Profile name={"Ram"} image={ram_avatar} text={"Ram is a 20 year old college student who is interested in technology. Outside of school he likes viewing sports, watching movies, and working out. He spends an average of two hours day on Social Media."} />
    , <Profile name={"Ram1"} image={ram_avatar} text="Testing" />, <Profile name={"Ram2"} image={ram_avatar} text={"Testing2"} />, <Profile name={"Ram3"} image={ram_avatar} text={"testing"} />]
  return (
    <div style={{ backgroundColor: '#FAF9F6', height: '100vh', width: '100%', minHeight: '100%' }}>
      <h1 className={modules.text}>
        Our Synthetic Users</h1>
      <div className={modules.rowstyle}>
        {Profiles.map((profile, index) => (
          <div> {profile} </div>
        ))}
      </div>
    </div>
  )
}
export default ProfileList; 
