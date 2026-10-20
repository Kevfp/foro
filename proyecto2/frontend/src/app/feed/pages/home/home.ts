import { Component, inject } from '@angular/core';
import { rxResource } from '@angular/core/rxjs-interop';
import { CategoryService } from '../../services/category-service.service';
import { JsonPipe } from '@angular/common';

@Component({
  selector: 'home',
  imports: [
    JsonPipe
  ],
  templateUrl: './home.html',
})
export class Home {

  categoryService = inject(CategoryService);

  categoryResource = rxResource({
    stream: () => this.categoryService.getCategories(),
  })
}
