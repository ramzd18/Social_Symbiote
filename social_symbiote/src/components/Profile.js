function Profile(props) {
  return (
    <div style={{ maxWidth: "200px", margin: "1rem" }}>
      <img src={props.image} style={{ width: '50%', height: '50%' }}></img>
      <h1>{props.name}</h1>
      <p>{props.text}</p>
    </div>
  )
}
export default Profile; 