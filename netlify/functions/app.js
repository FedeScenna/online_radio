const { spawn } = require('child_process');
const path = require('path');

exports.handler = async function(event, context) {
  const pythonScript = path.join(__dirname, 'app.py');
  
  try {
    const python = spawn('python', [pythonScript, JSON.stringify(event)]);
    
    let result = '';
    let error = '';

    await new Promise((resolve, reject) => {
      python.stdout.on('data', (data) => {
        result += data.toString();
      });

      python.stderr.on('data', (data) => {
        error += data.toString();
      });

      python.on('close', (code) => {
        if (code !== 0) {
          reject(new Error(`Python process exited with code ${code}: ${error}`));
        } else {
          resolve();
        }
      });
    });

    return JSON.parse(result);
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Internal Server Error' })
    };
  }
}; 