export default function ({ store, redirect }) {
  // Redirect to home page if the application is not running in development
  // mode
  if (process.env.NODE_ENV !== 'production') {
    return redirect('/')
  }
}
