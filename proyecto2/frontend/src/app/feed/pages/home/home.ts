import { Component, inject } from '@angular/core';
import { rxResource } from '@angular/core/rxjs-interop';
import { CategoryService } from '../../services/category-service.service';
import { JsonPipe } from '@angular/common';
import { RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'home',
  imports: [
    RouterLink,
    RouterLinkActive
  ],
  templateUrl: './home.html',
})
export class Home {

  categoryService = inject(CategoryService);

  categoryResource = rxResource({
    stream: () => this.categoryService.getCategories(),
  })


  linkMap = new Map<string,string>(
  [
    ["Entretemento", "entertainment"],
    ["Arte", "art"],
    ["Ciencia", "science"],
    ["Deporte", "sports"]
  ]
  )
}
