import { Component, signal } from '@angular/core';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { RouterOutlet } from '@angular/router';
import { SidenavComponent } from './pages/sidenav/sidenav.component';

@Component({
  selector: 'fn-root',
  imports: [
    RouterOutlet,
    MatSidenavModule,
    MatButtonModule,
    MatIconModule,
    SidenavComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'financier';

  isSideNavOpen = signal<boolean>(true);

  toggleSideNav() {
    this.isSideNavOpen.update((currentStatus) => !currentStatus);
  }
}
