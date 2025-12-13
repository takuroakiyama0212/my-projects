export interface Resource {
  id: string;
  title: string;
  description: string;
  url: string;
  type: 'tool' | 'video' | 'paper';
  category: string;
  tags: string[];
  featured: boolean;
  author: string;
}
