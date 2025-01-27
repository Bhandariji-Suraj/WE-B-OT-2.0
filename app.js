document.getElementById("searchBtn").addEventListener("click", async () => {
    const query = document.getElementById("query").value;
    const resultsContainer = document.getElementById("results");
    resultsContainer.innerHTML = "";
    if (!query) {
        alert("Please enter a query");
        return;
    }
    const response = await fetch("http://127.0.0.1:5000/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ query }),
    });
    const results = await response.json();
    results.forEach(result => {
        const li = document.createElement("li");
        li.innerHTML = `<a href="${result.link}" target="_blank">${result.link}</a> (Score: ${result.score.toFixed(2)})`;
        resultsContainer.appendChild(li);
    });
});
