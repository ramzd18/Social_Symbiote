// Define the valid roles for a chat
const validChatRoles = ['assistant', 'user', 'system'];

// Define an interface for a chat message
const ChatMessage = {
  content: '', // Message content
  role: validChatRoles[0], // Role of the message sender
};

function setRole(newRole) {
    if (validChatRoles.includes(newRole)) {
      ChatMessage.role = newRole;
    } else {
      throw new Error('Invalid chat role');
    }
  }

// Define an interface for a Persona
{/*const Persona = {
  id: undefined, // Unique identifier for the persona
  role: '', // Role of the persona ('assistant', 'user', or 'system')
  avatar: undefined, // URL of the persona's avatar
  name: '', // Name of the persona
  prompt: '', // Prompt for the persona
  key: '', // Key for the persona
  isDefault: false, // Boolean to indicate if it's a default persona
}; */}

// Define the structure of a chat
const Chat = {
  id: '', // Unique identifier for the chat
  // persona: undefined, // Persona object associated with the chat
  messages: [], // Array to store chat messages (using the ChatMessage structure)
};
