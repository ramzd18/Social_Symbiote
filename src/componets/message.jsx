const Message = (props) => {
    const { role, content } = props.message;
    const isUser = role === 'user';
  
    return (
        <div className="col-md-8 big">
            {isUser ? ( // Conditionally render sent-message or received-message
                <div class="sent-message">
                <img src="./Users Icons.svg" alt="" />
                <p>{content}</p> {/* Assuming 'content' is the message text */}
                </div>
            ) : (
                <div class="received-message">
                <img src="./Users Icons.svg" alt="" />
                <p>{content}</p>
                </div>
          )}
          </div>
    );
  };
  
  export default Message;