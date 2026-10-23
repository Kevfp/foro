import { Component, inject, OnInit } from '@angular/core';
import { CategoryService } from '../../services/category-service.service';
import { Subcategory } from '@interfaces/forum.interfaces';
import { rxResource } from '@angular/core/rxjs-interop';

@Component({
  selector: 'entertainment',
  imports: [],
  templateUrl: './entertainment.html',
})
export class Entertainment {

  categoryService = inject(CategoryService);
  subcategories: Subcategory[] = []

  subcategoryResource= rxResource({
    params: () => ({id: 1}),
    stream: ({params}) => this.categoryService.getSubcategories(params.id)
  })
}
