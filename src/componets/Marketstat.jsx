import ProgressCircle from "./ProgressCircle";
function Marketstat({ clarity, personalization, impact, retention, message }) {

  const rowStyle = {
    display: 'flex',
    flexDirection: 'row',
  };

  return (
    <div>
      <div style={rowStyle}>
        <div style={{ margin: '15px', textAlign: 'center' }}>

          <h1> Clarity </h1><ProgressCircle progress={clarity} />
        </div>
        <div style={{
          margin: '15px', textAlign: 'center'
        }}>
          <h1> Personalization</h1>
          <ProgressCircle progress={personalization} />
        </div>

        <div style={{ margin: '15px', textAlign: 'center' }}> <h1> Impact </h1><ProgressCircle progress={impact} />
        </div>
        <div style={{ margin: '15px', textAlign: 'center' }}>
          <h1> Retention</h1>
          <ProgressCircle progress={retention} />
        </div>
      </div>
      <h1> This is the message, {message} </h1>
    </div>

  );
}
export { Marketstat };