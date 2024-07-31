import { createClient } from 'redis';

const client = createClient()
  .on('error', err => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'));

async function setNewSchool(schoolName, value) {
  const reply = await client.set(schoolName, value);
  console.log(`Reply: ${reply}`);
}

async function displaySchoolValue(schoolName) {
  const value = await client.get(schoolName);
  console.log(value);
}

client.on('ready', async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
});
