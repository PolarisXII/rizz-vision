
import { Route, Switch } from 'wouter'
import './App.css'
import Landing from './pages/landing'
import Birthday from './pages/birthday'
import Name from './pages/name'
function App() {
 

  return (
    <Switch>
       <Route path="/" component={Landing} />
       <Route path="/details/age" component={Birthday} />
       <Route path="/details/name" component={Name} />
    </Switch>
    
  )
}

export default App
