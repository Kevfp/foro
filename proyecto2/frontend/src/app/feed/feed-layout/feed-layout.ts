import { Component } from '@angular/core';
import { Navbar } from '@shared/components/navbar/navbar';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'feed-layout',
  imports: [
    Navbar,
    RouterOutlet
  ],
  templateUrl: './feed-layout.html',
})
export class FeedLayout {}
