import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'shorten',
})
export class ShortenPipe implements PipeTransform {
  transform(value: string, length: number, limiter: string): string {
    return value.length > length
      ? value.substring(0, length).trim() + limiter
      : value;
  }
}
