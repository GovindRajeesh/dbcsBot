document.addEventListener('DOMContentLoaded', () => {
  const chatForm = document.getElementById('chat-form');
  const chatLog = document.getElementById('chat-log');
  const userMessageInput = document.getElementById('user-message');

  chatForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const userMessage = userMessageInput.value;
    if (userMessage.trim() === '') {
      return;
    }

    displayMessage('User', userMessage, scroll = false);
    userMessageInput.value = '';

    sendChatMessage(userMessage);
  });

  function displayMessage(sender, message, scroll = true) {
    const messageContainer = document.createElement('div');
    messageContainer.classList.add('message-container');

    const senderElement = document.createElement('span');
    senderElement.classList.add('sender');
    senderElement.innerText = sender + ':';

    const messageElement = document.createElement('span');
    messageElement.classList.add('message');
    messageElement.innerText = message;

    messageContainer.appendChild(senderElement);

    var sv;
    if (scroll) {
      chatLog.scrollTop = chatLog.scrollHeight + 100;
      sv = chatLog.scrollTop
    }
    messageContainer.appendChild(messageElement);
    if (scroll) {
      chatLog.scrollTop = sv + 100;
    }

    chatLog.appendChild(messageContainer);
  }

  function sendChatMessage(message) {
    userMessageInput.value = "Loading..."
    userMessageInput.disabled = true
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/chat', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        const response = JSON.parse(xhr.responseText).response;
        displayMessage('Chatbot', response.replace(/\n/g, "\n"));
        userMessageInput.disabled = false
        userMessageInput.value = ''
      }
    };
    const requestBody = JSON.stringify({ 'message': message }); // Ensure 'message' key is included in the request body
    xhr.send(requestBody);
  }

});
