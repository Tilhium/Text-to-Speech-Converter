document.addEventListener("DOMContentLoaded", () => {
    const textInput = document.getElementById("textInput");
    const readBtn = document.getElementById("readBtn");
    const reverseReadBtn = document.getElementById("reverseReadBtn");
    const voiceSelect = document.getElementById("voiceSelect");
    const audioPlayer = document.getElementById("audioPlayer");

    function speak(url) {
        const randomParam = new Date().getTime(); // Önbellek önleme için zaman damgası
        audioPlayer.src = `${url}?t=${randomParam}`;
        audioPlayer.hidden = false;
        audioPlayer.load();
        audioPlayer.play();
    }

    async function fetchAudio(endpoint) {
        const text = textInput.value.trim();
        const lang = voiceSelect.value;

        if (!text) return;

        try {
            const response = await fetch(endpoint, {
                method: "POST",
                body: new URLSearchParams({ text, lang }),
                headers: { "Content-Type": "application/x-www-form-urlencoded" }
            });

            if (response.ok) {
                const data = await response.json();
                const audioUrl = data.audio_url;
                console.log("Audio URL:", audioUrl);
                speak(audioUrl);
            } else {
                console.error('Error:', response.status);
            }
        } catch (error) {
            console.error("Fetch error:", error);
        }
    }

    readBtn.addEventListener("click", () => fetchAudio("/speak"));
    reverseReadBtn.addEventListener("click", () => fetchAudio("/reverse_speak"));
});
