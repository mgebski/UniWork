const db = require('./db');


async function getMultiple(){
  
  const rows = await db.query(
    'SELECT * from login', 
  );
  const data = rows;
  return {
    data
    
  }
}


async function create(user){
  const result = await db.query(
    
    `INSERT INTO login 
    (email, password, calories) 
    VALUES 
    (?, ?, ?)`, 
    [
      user.email, user.password,
      user.calories
    ]
  )

}
async function updateCalories(user){
  const result = await db.query(
    `UPDATE login 
     set
     calories=? 
     WHERE email=? `, 
    [
      user.calories,user.email
    ]
  )

}
async function getCalories(user){
  const rows = await db.query(
    `SELECT calories from login 
     where email=? `,
  [
    user.email
  ]
  
  )
  const data = rows;
  return {
    data
    
  }

}
module.exports = {
  getMultiple,
  create,
  updateCalories,
  getCalories
}