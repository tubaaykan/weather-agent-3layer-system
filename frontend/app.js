//frontend’in konuştuğu backend sunucusudur
//frontend ile database/API arasında köprü kuran backend dosyasıdır



// Hava durumu bilgisi almak için async (asenkron) fonksiyon
// async → içinde await kullanabilmemizi sağlar
async function getWeather() {

    // HTML içindeki input alanını buluyoruz ve kullanıcı değerini alıyoruz
    const input = document.getElementById("input").value;

    // Backend API'ye (FastAPI vs.) istek gönderiyoruz
    // fetch → HTTP request atar
    const res = await fetch("http://127.0.0.1:8000/weather", {

        // İstek türü: POST (veri gönderiyoruz)
        method: "POST",

        // Header kısmı: gönderdiğimiz verinin JSON olduğunu söylüyoruz
        headers: {
            "Content-Type": "application/json"
        },

        // Backend'e gönderilen veri
        // input'u JSON formatına çeviriyoruz
        body: JSON.stringify({ text: input })
    });

    // Backend'den gelen cevabı JSON formatına çeviriyoruz
    const data = await res.json();

    // Sonucu HTML'deki "result" alanına yazdırıyoruz
    document.getElementById("result").innerText =
        `${data.city}: ${data.temp}°C, ${data.description}`;
}