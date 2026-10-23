export interface Category {
  id:              number;
  title:           string;
  description:     string;
  subcategories?:  Subcategory[];
  position:        number;
  parent_category: null;
}

export interface Subcategory {
  id:              number;
  title:           string;
  description:     string;
  position:        number;
  parent_category: number;
}
