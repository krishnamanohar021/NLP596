async function compare() {
    const prompt = document.getElementById("prompt").ariaValueMax;

    const response = await fetch("http://127.0.01:8000/compare", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body:JSON.stringify({prompt})
    });

    const data = await response.json();

    document.getElementById("openai").innerText = data.OpenAI;
    document.getElementById("claude").innerText = data.calude;
    document.getElementById("gemini").innerText = data.Gemini;

}