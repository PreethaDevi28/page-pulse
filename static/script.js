async function auditWebsite() {

    const url = document.getElementById("url").value.trim();

    const result = document.getElementById("result");

    const loader = document.getElementById("loader");

    if (url === "") {

        result.innerHTML = `
        <div class="result-card">
            <h2>⚠️ Missing URL</h2>
            <p>Please enter a website URL.</p>
        </div>
        `;

        return;
    }

    loader.classList.remove("hidden");

    result.innerHTML = "";

    try {

        const response = await fetch("/audit", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                url: url
            })

        });

        const data = await response.json();

        loader.classList.add("hidden");

        if (data.error) {

            result.innerHTML = `
            <div class="result-card">

                <h2>❌ Audit Failed</h2>

                <p class="error">${data.error}</p>

            </div>
            `;

            return;
        }

        result.innerHTML = `

        <div class="result-card">

            <h2>📊 Website Audit Report</h2>

            <div class="stats-grid">

                <div class="stat-box">
                    <h3>🌐 HTTP Status</h3>
                    <span>${data.status}</span>
                </div>

                <div class="stat-box">
                    <h3>⚡ Response Time</h3>
                    <span>${data.response_time} sec</span>
                </div>

                <div class="stat-box">
                    <h3>🏷️ H1 Tags</h3>
                    <span>${data.h1_count}</span>
                </div>

                <div class="stat-box">
                    <h3>🖼 Images</h3>
                    <span>${data.image_count}</span>
                </div>

                <div class="stat-box">
                    <h3>📚 Word Count</h3>
                    <span>${data.word_count}</span>
                </div>

            </div>

            <div class="info-box">

                <h3>📄 Page Title</h3>

                <p>${data.title}</p>

            </div>

            <div class="info-box">

                <h3>📝 Meta Description</h3>

                <p>${data.meta_description}</p>

            </div>

        </div>

        `;

    }

    catch (error) {

        loader.classList.add("hidden");

        result.innerHTML = `
        <div class="result-card">

            <h2>❌ Server Error</h2>

            <p class="error">
            Unable to connect to the Flask server.
            </p>

        </div>
        `;

    }

}