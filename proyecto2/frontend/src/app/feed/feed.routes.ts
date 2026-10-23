import { Routes } from '@angular/router';
import { FeedLayout } from './feed-layout/feed-layout';
import { Home } from './pages/home/home';
import { Entertainment } from './pages/entertainment/entertainment';

const feedRoutes: Routes = [
  {
    path: "",
    component: FeedLayout,
    children: [
      {
        path: "",
        component: Home
      },
      {
        path: "entertainment",
        component: Entertainment
      }
    ]
  }
];

export default feedRoutes;
