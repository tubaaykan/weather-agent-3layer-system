async function getWeather() {
    const input = document.getElementById("input").value.trim();
    const resultDiv = document.getElementById("result");

    // Boş input kontrolü
    if (!input) {
        resultDiv.innerText = "⚠️ Lütfen bir şehir adı girin.";
        resultDiv.className = "error";
        return;
    }

    // Yükleniyor göster
    resultDiv.innerText = "🔄 Yükleniyor...";
    resultDiv.className = "";

    try {
        const res = await fetch("http://127.0.0.1:8000/weather", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: input })
        });

        // HTTP seviyesinde hata kontrolü
        if (!res.ok) {
            throw new Error(`Sunucu hatası: ${res.status}`);
        }

        const data = await res.json();

        // Backend'den hata geldiyse göster
        if (data.error) {
            resultDiv.innerText = `❌ ${data.error}`;
            resultDiv.className = "error";
            return;
        }

        // Başarılı yanıt — detaylı göster
        resultDiv.innerHTML = `
            <div class="weather-card">
                <h2>📍 ${data.city}</h2>
                <div class="temp">${data.temp}°C</div>
                <div class="desc">${data.description}</div>
                <div class="details">
                    <span>🌡 Hissedilen: ${data.feels_like}°C</span>
                    <span>💧 Nem: %${data.humidity}</span>
                    <span>💨 Rüzgar: ${data.wind_speed} m/s</span>
                </div>
            </div>
        `;
        resultDiv.className = "success";

    } catch (err) {
        // Bağlantı hatası (backend çalışmıyor vs.)
        console.error("Fetch hatası:", err);
        resultDiv.innerText = "❌ Backend'e bağlanılamadı. Sunucunun çalıştığından emin olun.";
        resultDiv.className = "error";
    }
}

// Enter tuşuyla da çalışsın
document.getElementById("input").addEventListener("keydown", function(e) {
    if (e.key === "Enter") getWeather();
});
