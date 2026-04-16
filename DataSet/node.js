const fs = require('fs');

function searchOffice(query) {
    try {
        // JSON file read kora hocche
        const rawData = fs.readFileSync('ContactData.json');
        const data = JSON.parse(rawData);

        const lowerQuery = query.toLowerCase().trim();

        // Filter algorithm
        const results = data.filter(office => {
            const city = (office.city || "").toLowerCase();
            const address = (office.address || "").toLowerCase();
            const name = (office.name || "").toLowerCase();

            return city.includes(lowerQuery) || 
                   address.includes(lowerQuery) || 
                   name.includes(lowerQuery);
        });

        // Result display
        if (results.length > 0) {
            console.log(`Total ${results.length} ti office pauya geche:\n`);
            results.forEach((office, index) => {
                console.log(`${index + 1}. Name: ${office.name}`);
                console.log(`   Address: ${office.address}`);
                console.log(`   Phone: ${office.phone1}`);
                console.log(`   City: ${office.city}`);
                console.log('----------------------------');
            });
        } else {
            console.log("Kono result pauya jai ni.");
        }
    } catch (err) {
        console.error("Error reading file:", err.message);
    }
}

// Search check korar jonno
searchOffice("Dhaka");