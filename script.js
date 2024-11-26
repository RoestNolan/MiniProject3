async function getResponse(prompt) {
    const response = await fetch('https://<your-heroku-app>.herokuapp.com/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: prompt }),
    });

    const data = await response.json();
    return data.response;
}

async function sendMessage() {
    const prompt = document.getElementById("prompt").value;
    const model1Response = await getResponse(prompt);

    // Show model 1 response
    document.getElementById("model1-chat").innerText = model1Response;

    // Generate model 2 response based on model 1's output
    const model2Response = await getResponse(model1Response);
    document.getElementById("model2-chat").innerText = model2Response;
}
