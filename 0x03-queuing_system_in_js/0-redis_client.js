import { createClient } from 'redis';

(async () => {
  try {
    const client = await createClient()
      .on('error', err => console.log(`Redis client not connected to the server: ${err}`));
    console.log('Redis client connected to the server');
  } catch (err) {
    console.log(err);
  }
})();
