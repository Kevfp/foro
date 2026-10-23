import { HttpClient } from '@angular/common/http';
import { inject, Service } from '@angular/core';
import { environmentDev } from '@environment/environment.development';
import { Category, Subcategory } from '@interfaces/forum.interfaces';
import { catchError, map, of, tap } from 'rxjs';

@Service()
export class CategoryService {

  url = environmentDev.base_url;

  http = inject(HttpClient);

  getCategories(){
    return this.http.get<Category[]>(`${this.url}/forum/category/`).
    pipe(
      catchError((error) =>{
        console.log(error);
        return of([]);
      }
    )
    );
  }

  getCategory(id: number){
    return this.http.get<Category>(`${this.url}/forum/category/${id}/`).
    pipe(
      // catchError((error)=>{
      //   console.log(error);
      //   return of([]);
      // })
    )
  }

  getSubcategories(id:number){
    const subcategories: Subcategory[] = [];
    return this.getCategory(id).pipe(
      map((response) => {
        response.subcategories?.forEach((subcategory) => subcategories.push(subcategory))
        return subcategories;
      },
    catchError((error) => {
      console.log(error);
      return of([])
    }))
    )
  }
}
