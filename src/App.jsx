import './App.css'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import ViewAllData from './pages/AllData/ViewAllData';
import Test from './pages/Test/Test';

const router = createBrowserRouter([
  {
    path: "/",
    element: <ViewAllData />,
  },
  {
    path: "/test",
    element: <Test />,
  }
]);

function App() {

  return (
    <RouterProvider router={router} />
  )
}

export default App
