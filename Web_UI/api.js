const url = 'https://faq-generator.loca.lt/api'

function get_faq(_context)
{
    console.log("Fetching API Data");
    console.time("timer")
    fetch(url, {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            // context: _context;
            context: "Delhi is the capital of India.",
            limit: 5
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        console.timeEnd("timer");
    });
}