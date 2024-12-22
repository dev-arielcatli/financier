import { Component } from '@angular/core';
import { MatListModule } from '@angular/material/list';
import { NAVIGATION_ITEMS } from './sidenav.config';
import { MatIconModule } from '@angular/material/icon';
import { RouterLink } from '@angular/router';
import { Navigation } from './sidenav.model';

@Component({
  selector: 'fn-sidenav',
  imports: [MatListModule, MatIconModule, RouterLink],
  templateUrl: './sidenav.component.html',
  styleUrl: './sidenav.component.scss',
})
export class SidenavComponent {
  NAVIGATION_ITEMS = [...NAVIGATION_ITEMS];

  setActive(item: Navigation) {
    if (item.disabled) {
      return;
    }
    this.NAVIGATION_ITEMS = this.NAVIGATION_ITEMS.map((navItem) => {
      if (navItem.id === item.id) {
        return { ...navItem, active: true };
      }

      return { ...navItem, active: false };
    });
  }
}
