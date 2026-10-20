import { Routes } from '@angular/router';
import { FeedLayout } from './feed-layout/feed-layout';
import { Home } from './pages/home/home';

const feedRoutes: Routes = [
  {
    path: "",
    component: FeedLayout,
    children: [
      {
        path: "",
        component: Home
      }
    ]
  }
];

export default feedRoutes;
