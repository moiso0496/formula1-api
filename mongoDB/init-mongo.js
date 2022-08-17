db.createUser(
    {
        user: "api_user",
        pwd: "apipassword",
        roles: [
            {
                role: "readWrite",
                db: "fsd-formula1"
            }
        ]
    });

db.createCollection('drivers');
db.getCollection('drivers').createIndex({driver_num:1}, {unique:true})
