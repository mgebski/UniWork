const express = require('express');
const router = express.Router();
const users = require('../services/fitnessusers');

router.get('/', async function(req, res, next) {
  try {
    res.json(await users.getMultiple());
  } catch (err) {
    console.error(`Error `, err.message);
    next(err);
  }
});
router.post('/adduser', async function(req, res, next) {
  try {
    res.json(await users.create(req.body));
  } catch (err) {
    console.error(`Error`, err.message);
    next(err);
  }
});
router.put('/updatecalories', async function(req, res, next) {
  try {
    res.json(await users.updateCalories( req.body));
  } catch (err) {
    console.error(`Error`, err.message);
    next(err);
  }
});
router.post('/getCalories', async function(req, res, next) {
  try {
    res.json(await users.getCalories(req.body));
  } catch (err) {
    console.error(`Error`, err.message);
    next(err);
  }
});
module.exports = router;