export default function handleResponseFromAPI(promise) {
  const success = true
  return new Promise((resolve, reject) => {
    if (success) {
      resolve ( { 'status': 200, body: 'success' } )
      console.log('Got a response from the API')
    }
    else {
      reject(new Error(''))
      console.log('Got a response from the API')
    }
  })
}
