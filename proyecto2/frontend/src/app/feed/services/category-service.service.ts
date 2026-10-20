import { HttpClient } from '@angular/common/http';
import { inject, Service } from '@angular/core';
import { environmentDev } from '@environment/environment.development';
import { Category } from '@interfaces/forum.interfaces';
import { catchError, of, tap } from 'rxjs';

@Service()
export class CategoryService {

  url = environmentDev.base_url;

  http = inject(HttpClient);

  getCategories(){
    console.log(`${this.url}/forum/category/`);
    return this.http.get<Category[]>(`${this.url}/forum/category/`).
    pipe(
      tap((results) => console.log(results)),
      catchError((error) =>{
        console.log(error);
        return of([]);
      }
    )
    );
  }
}
