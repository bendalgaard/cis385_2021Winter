# CIS385_Assignment5
CIS385_Assignment5

Create an Angular project using the provided REST API.

Run these commands to create a sample MongoDb collection
```javascript
use bidding
db.createCollection('items')
db.items.insertOne({ name: "iPhone 5s", description: "Apple iPhone 5s - Verizon", startingPrice: 100, bids: [ { username: "bdalgaard", price: 120 } ] } )
db.items.insertOne( { name: "Nexus 6P", description: "Google Nexus 6P", startingPrice: 200, bids: [ { username: "bdalgaard", price: 220, } ] } )
```
